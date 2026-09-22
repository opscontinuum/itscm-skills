"""Build the ISCP data-collection workbook.

This is a BUILD TOOL, not a skill. The repository's no-interpreter rule governs
skills, which must work for a reader with no filesystem. This script produces an
artifact that such a reader fills in by hand.

Run:  python3 build_workbook.py  ->  iscp-data-collection.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

ROWS = 200  # how far every dropdown and every entry range extends

HEAD = PatternFill("solid", fgColor="1F3864")
HEAD_FONT = Font(color="FFFFFF", bold=True, size=11)
NOTE_FONT = Font(italic=True, color="595959", size=9)
TITLE_FONT = Font(bold=True, size=14, color="1F3864")
DERIVED = PatternFill("solid", fgColor="FFF2CC")
REQUIRED = PatternFill("solid", fgColor="FCE4D6")
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

wb = Workbook()


def sheet(title, blurb, headers, widths, notes=None):
    ws = wb.create_sheet(title)
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = blurb
    ws["A2"].font = NOTE_FONT
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(len(headers), 6))
    ws.row_dimensions[2].height = 30
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=4, column=i, value=h)
        c.fill = HEAD
        c.font = HEAD_FONT
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = THIN
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.row_dimensions[4].height = 32
    ws.freeze_panes = "A5"
    if notes:
        ws.cell(row=ROWS + 3, column=1, value=notes).font = NOTE_FONT
    return ws


def dropdown(ws, col, formula, first=5, last=ROWS):
    dv = DataValidation(type="list", formula1=formula, allow_blank=True, showDropDown=False)
    dv.error = "Pick a value from the list. If the value you need is not there, add it on the tab it comes from."
    dv.errorTitle = "Not on the list"
    ws.add_data_validation(dv)
    dv.add(f"{col}{first}:{col}{last}")


def name(ref_name, sheet_title, col):
    wb.defined_names.add(
        DefinedName(ref_name, attr_text=f"'{sheet_title}'!${col}$5:${col}${ROWS}")
    )


# ---------------------------------------------------------------- Start here
ws = wb.active
ws.title = "Start here"
ws.column_dimensions["A"].width = 118
ws["A1"] = "ISCP data collection"
ws["A1"].font = Font(bold=True, size=18, color="1F3864")

INTRO = [
    "",
    "This workbook collects everything needed to write an Information System Contingency Plan and,",
    "more importantly, everything needed to build a continuity program from one. Fill it in, then",
    "hand it to the iscp-from-worksheet skill.",
    "",
    "FILL THE TABS IN ORDER. Each one feeds the dropdowns on the next.",
    "",
    "  1  System              What you are planning for. Five minutes.",
    "  2  Processes           The business work this system carries. The foundation of everything below.",
    "  3  Impact scale        What severe, moderate and minimal mean here, in your terms.",
    "  4  Process impact      What an outage costs each process, on that scale.",
    "  5  Objectives          How long each process can be down, and how much data it can lose.",
    "  6  Resources           The components the system is made of.",
    "  7  Process-Resource    Which components each process depends on. DO NOT SKIP THIS TAB.",
    "  8  Priorities          What order to recover in. Mostly derived from tab 7.",
    "  9  Contacts            Who to call.",
    " 10  Vendors             Who to call outside the organization.",
    " 11  Sites and backups   Where else it can run, and what protects the data.",
    " 12  Approvals           Who agreed to all of it. Without this the numbers are nobody's.",
    "",
    "",
    "THREE THINGS PEOPLE GET WRONG, AND THE WHOLE POINT OF THIS WORKBOOK",
    "",
    "1. Recovery objectives belong to business processes, not to servers or tiers.",
    "   'The database is Tier 1, so four hours' is a fact about infrastructure. 'Payroll must run",
    "   within four hours or people are not paid on the statutory date' is the number you need.",
    "   Tab 5 will only let you enter objectives against a process from tab 2, on purpose.",
    "",
    "2. Tab 7 is the one everybody skips, and nothing works without it.",
    "   Standard BIA templates ask for processes, and for resources, and never ask which resources",
    "   each process uses. They do not forbid it either, and working out a recovery order requires it,",
    "   so this is a prerequisite rather than an extra. Without that link there is no way to get from",
    "   'payroll matters most' to 'therefore restore the database first', and no recovery order exists.",
    "",
    "3. These are the business's numbers, not IT's.",
    "   Do not work out an objective from what the system can currently do. State what the business",
    "   needs, then judge the architecture against it. That comparison is the entire value of the",
    "   exercise, and it disappears if the requirement is copied from the capability.",
    "",
    "",
    "HOW TO FILL A CELL YOU DO NOT KNOW",
    "",
    "Leave it blank. A blank cell is reported as missing and somebody gets asked.",
    "A guess is reported as an answer and nobody ever checks it again.",
    "",
    "Orange columns are required. Yellow columns are worked out from other tabs; fill them only to",
    "override, and say why in the notes column when you do.",
]
for i, line in enumerate(INTRO, start=2):
    c = ws.cell(row=i, column=1, value=line)
    if line.isupper() and line.strip():
        c.font = Font(bold=True, size=11, color="1F3864")
    elif line.strip().startswith(("1.", "2.", "3.")):
        c.font = Font(bold=True, size=10)

# ---------------------------------------------------------------- 1 System
ws = sheet(
    "1 System",
    "The system this plan covers. One row. If you are planning for several systems, use one workbook each: "
    "recovery objectives are per system and merging them hides which one is driving a number.",
    ["Field", "Value", "Notes"],
    [42, 56, 52],
)
FIELDS = [
    ("System name", "The name the business uses, not the hostname."),
    ("System unique identifier", "Inventory or FISMA identifier, if there is one."),
    ("System owner (name)", "A person. Not a team."),
    ("System owner (role and contact)", ""),
    ("Authorizing official", "Who accepts the risk. Often not the owner."),
    ("Operating organization", "Who runs it day to day."),
    ("FIPS 199 availability impact", "Low, Moderate or High. Drives which controls apply."),
    ("Hosting model", ""),
    ("Primary location or region", ""),
    ("Alternate location or region", "Blank if there is none. Blank is an answer here."),
    ("Availability commitment", "For example 99.9%. Blank if none was ever promised."),
    ("Availability measured over", "Monthly, annually, business hours only."),
    ("Plan owner", "Who keeps this plan current. Often not the system owner."),
    ("Date of this data collection", ""),
]
for i, (f, note) in enumerate(FIELDS, start=5):
    ws.cell(row=i, column=1, value=f).font = Font(bold=True)
    ws.cell(row=i, column=2).fill = REQUIRED
    ws.cell(row=i, column=2).border = THIN
    ws.cell(row=i, column=3, value=note).font = NOTE_FONT

dv = DataValidation(type="list", formula1='"Low,Moderate,High,Not categorized"', allow_blank=True)
ws.add_data_validation(dv); dv.add("B11")
dv = DataValidation(
    type="list",
    formula1='"Public cloud,Private cloud,Hybrid,On premises,SaaS,Co-located"',
    allow_blank=True,
)
ws.add_data_validation(dv); dv.add("B12")

# ---------------------------------------------------------------- 2 Processes
ws = sheet(
    "2 Processes",
    "The business work that stops when this system stops. Ask the people who own the work, not the people who own "
    "the servers. Write a description a non-engineer would recognize. Everything else in this workbook keys off "
    "this list, so get it complete before moving on.",
    ["Mission/Business process", "Description", "Process owner (name)", "Owner role", "Notes"],
    [34, 62, 26, 26, 40],
    notes="If a process has no named owner, write UNOWNED. It is a finding, not a blank.",
)
for r in range(5, ROWS + 1):
    for col in (1, 2, 3):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN
name("ProcessList", "2 Processes", "A")

# ---------------------------------------------------------------- 3 Impact scale
ws = sheet(
    "3 Impact scale",
    "What severe, moderate and minimal actually mean for this organization. Standards print example figures to "
    "show the shape of this table. Do not copy them. A scale borrowed from a standard describes that standard's "
    "illustration, and every impact rating you record against it afterwards is meaningless.",
    ["Impact category", "Severe", "Moderate", "Minimal"],
    [30, 44, 44, 44],
    notes="Common categories: financial, regulatory and contractual, customer and operational, workforce, "
          "reputational, safety. Use the ones this organization already argues about.",
)
for r in range(5, ROWS + 1):
    for col in range(1, 5):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN
name("CategoryList", "3 Impact scale", "A")

# ---------------------------------------------------------------- 4 Process impact
ws = sheet(
    "4 Process impact",
    "One row per process per impact category. Both columns are dropdowns fed by tabs 2 and 3, so you cannot rate a "
    "process that does not exist or use a category you have not defined. The overall rating is yours to judge: it is "
    "usually the worst single category rather than an average, because a business does not average a missed payroll.",
    ["Mission/Business process", "Impact category", "Rating", "What actually happens", "Overall rating for this process"],
    [34, 28, 16, 62, 26],
)
dropdown(ws, "A", "=ProcessList")
dropdown(ws, "B", "=CategoryList")
dropdown(ws, "C", '"Severe,Moderate,Minimal,Not assessed"')
dropdown(ws, "E", '"Severe,Moderate,Minimal,Not assessed"')
for r in range(5, ROWS + 1):
    for col in (1, 2, 3):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 5 Objectives
ws = sheet(
    "5 Objectives",
    "How long each process can be down (MTD), how fast the system must be technically back (RTO), and how much "
    "committed data it can afford to lose (RPO). RTO must be SHORTER than MTD, because work still has to be done "
    "after the system is available before the business is actually running. If a process behaves differently at "
    "certain times, month end or a payroll run, give it two rows and say so in the condition column.",
    ["Mission/Business process", "Condition", "MTD", "RTO", "RPO", "What drives the MTD",
     "Alternate way of working while it is down", "Committed?"],
    [30, 26, 13, 13, 13, 40, 48, 15],
    notes="Condition: leave blank for the normal case. Use it for 'within month-end close', 'within 48 hr of "
          "payroll' and similar. Alternate way of working: if there is none, write NONE. That is the answer, not a gap.",
)
dropdown(ws, "A", "=ProcessList")
dropdown(ws, "F", '"Statutory deadline,Contractual obligation,Revenue loss rate,Customer tolerance,'
                  'Workload backlog,Internal convenience,Not established"')
dropdown(ws, "H", '"Agreed and signed,Proposed only,Inherited from a default,Unknown"')
for r in range(5, ROWS + 1):
    for col in (1, 3, 4, 5, 6, 8):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 6 Resources
ws = sheet(
    "6 Resources",
    "The components this system is made of. Group them logically rather than listing every host: 'application tier "
    "nodes' is more useful than eleven server names. The test is whether you would recover them together.",
    ["System resource or component", "Platform / OS / version", "Description", "Where it runs", "Notes"],
    [34, 30, 52, 26, 34],
)
for r in range(5, ROWS + 1):
    for col in (1, 3):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN
name("ResourceList", "6 Resources", "A")

# ---------------------------------------------------------------- 7 The join
ws = sheet(
    "7 Process-Resource",
    "THE TAB EVERYBODY SKIPS. One row for every pairing: which components does each process actually need in order "
    "to work? Both columns are dropdowns, so you cannot invent either side. Without this tab there is no way to turn "
    "'payroll matters most' into 'therefore restore the database first', and no recovery order can be produced at all. "
    "No standard template prompts for this and none forbids it: working out a recovery order requires it, "
    "so it is a prerequisite rather than an extra. That is why so many plans cannot answer what to fix first.",
    ["Mission/Business process", "Depends on this resource", "Essential or degraded?", "Notes"],
    [34, 34, 24, 52],
    notes="Essential: the process cannot run at all without it. Degraded: the process runs in a reduced form. "
          "Mark honestly. Everything marked essential inherits that process's recovery time on tab 8.",
)
dropdown(ws, "A", "=ProcessList")
dropdown(ws, "B", "=ResourceList")
dropdown(ws, "C", '"Essential,Degraded,Not needed"')
for r in range(5, ROWS + 1):
    for col in (1, 2, 3):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 8 Priorities
ws = sheet(
    "8 Priorities",
    "What order to bring things back in. Mostly worked out for you: a resource inherits the tightest RTO of any "
    "process that depends on it as essential (tabs 5 and 7). Fill the yellow columns only to override, and say why. "
    "An override with no reason is how a recovery order stops matching the business.",
    ["Priority", "System resource or component", "Recovery time objective", "Set by which process",
     "Override reason (only if you changed it)"],
    [11, 34, 22, 34, 52],
)
dropdown(ws, "B", "=ResourceList")
for r in range(5, ROWS + 1):
    for col in (1, 3, 4):
        ws.cell(row=r, column=col).fill = DERIVED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 9 Contacts
ws = sheet(
    "9 Contacts",
    "Who gets called, in what order. Include the deputy for every role: the plan is used at 3am and on holidays, "
    "which is exactly when the first name is unreachable.",
    ["Role on the recovery team", "Name", "Job title", "Work phone", "Mobile", "Email",
     "Alternate for which role?", "Position in call tree"],
    [28, 24, 26, 18, 18, 30, 26, 18],
    notes="Position in call tree: 1 for whoever is called first. Ties are fine; they mean called in parallel.",
)
for r in range(5, ROWS + 1):
    for col in (1, 2, 5, 6):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 10 Vendors
ws = sheet(
    "10 Vendors",
    "Outside parties you would have to call. A support contract nobody can find the number for at 3am is not a "
    "support contract. Record the identifier you must quote to get service, because that is what actually gets asked for.",
    ["Vendor or partner", "Product or service", "Contract, account or support ID", "Support phone",
     "Service level promised", "Escalation path", "Notes"],
    [28, 28, 30, 20, 26, 30, 30],
)
for r in range(5, ROWS + 1):
    for col in (1, 2, 3, 4):
        ws.cell(row=r, column=col).fill = REQUIRED
        ws.cell(row=r, column=col).border = THIN

# ---------------------------------------------------------------- 11 Sites and backups
ws = sheet(
    "11 Sites and backups",
    "Where else this can run, and what protects the data. The second table is the one that decides whether your RPO "
    "on tab 5 is real or aspirational, so answer the last two columns honestly.",
    ["Entry type", "Name or designation", "Type", "Location or address", "What it can run",
     "How long to bring it up", "Notes"],
    [20, 28, 22, 34, 32, 22, 34],
)
dropdown(ws, "A", '"Alternate site,Alternate storage,Alternate telecom"')
dropdown(ws, "C", '"Cold site,Warm site,Hot site,Mirrored site,Cloud region,Not applicable"')

r0 = ROWS + 6
ws.cell(row=r0, column=1, value="What protects the data").font = TITLE_FONT
BACK_HEADS = ["Resource protected", "Mechanism", "How often", "Kept for how long", "Stored where",
              "Survives loss of the primary site?", "Last restore actually performed"]
for i, h in enumerate(BACK_HEADS, start=1):
    c = ws.cell(row=r0 + 2, column=i, value=h)
    c.fill = HEAD; c.font = HEAD_FONT; c.border = THIN
    c.alignment = Alignment(wrap_text=True, vertical="center")
ws.row_dimensions[r0 + 2].height = 32
dropdown(ws, "A", "=ResourceList", first=r0 + 3, last=r0 + 60)
dv = DataValidation(type="list", allow_blank=True,
                    formula1='"Synchronous replication,Asynchronous replication,Snapshot,Full backup,'
                             'Incremental backup,Differential backup,Object replication,None"')
ws.add_data_validation(dv); dv.add(f"B{r0+3}:B{r0+60}")
dv = DataValidation(type="list", formula1='"Yes,No,Not known"', allow_blank=True)
ws.add_data_validation(dv); dv.add(f"F{r0+3}:F{r0+60}")
ws.cell(row=r0 + 62, column=1,
        value="Last restore actually performed: a date, or NEVER. 'We take backups' and 'we have restored from "
              "backup' are separated by the entire risk, and only the second one is evidence.").font = NOTE_FONT

# ---------------------------------------------------------------- 12 Approvals
ws = sheet(
    "12 Approvals",
    "Who agreed to the numbers on tab 5. This is what turns them from a proposal into a commitment. Objectives with "
    "no signature are design targets: they describe what somebody hoped for, and they cannot be missed, because "
    "nobody promised them.",
    ["Role", "Name", "What they are agreeing to", "Signed?", "Date"],
    [32, 26, 54, 16, 16],
)
APPROVERS = [
    ("System owner", "The system description and the resource list"),
    ("Business owner", "The processes, their impact ratings, and the MTDs"),
    ("Finance", "The financial impact thresholds on tab 3"),
    ("Authorizing official", "The residual risk of the objectives as stated"),
    ("Plan owner", "That this plan will be kept current and tested"),
]
for i, (role, what) in enumerate(APPROVERS, start=5):
    ws.cell(row=i, column=1, value=role).font = Font(bold=True)
    ws.cell(row=i, column=3, value=what)
    for col in (2, 4, 5):
        ws.cell(row=i, column=col).fill = REQUIRED
        ws.cell(row=i, column=col).border = THIN
dv = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
ws.add_data_validation(dv); dv.add("D5:D20")

wb.save("iscp-data-collection.xlsx")
print("wrote iscp-data-collection.xlsx")

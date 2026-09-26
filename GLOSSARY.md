# Glossary

Every acronym used anywhere in this repository.

Each document also carries its own short table of the terms it uses, because a skill is read on
its own and a reader who has to leave the page to understand it has been sent somewhere they may
not be able to go.

| | Stands for | Notes |
|---|---|---|
| **AD** | availability domain | An isolated fault domain inside a cloud region |
| **AP** | accounts payable |  |
| **APM** | application performance monitoring |  |
| **AR** | accounts receivable |  |
| **BCP** | Business Continuity Plan | Outside ISCP scope |
| **BI** | business intelligence |  |
| **BIA** | Business Impact Analysis | The analysis that produces the processes, their impacts and their recovery objectives |
| **CI** | configuration item |  |
| **CMDB** | configuration management database |  |
| **CNSSI** | Committee on National Security Systems Instruction |  |
| **COOP** | Continuity of Operations Plan | Outside ISCP scope |
| **CP** | Contingency Planning | The NIST SP 800-53 control family |
| **CSO** | Cloud Service Offering | FedRAMP term |
| **DNS** | Domain Name System | Resolves names to addresses. Usually needed to recover, and easy to leave inside the failure domain |
| **DR** | disaster recovery |  |
| **DRP** | Disaster Recovery Plan | Neither FedRAMP nor NIST publishes a template for one |
| **EBS** | E-Business Suite | Oracle ERP |
| **EDI** | electronic data interchange |  |
| **ERP** | enterprise resource planning |  |
| **FIPS** | Federal Information Processing Standards |  |
| **GL** | general ledger |  |
| **ISCP** | Information System Contingency Plan | A system-level plan under NIST SP 800-34 and FedRAMP |
| **IT** | information technology |  |
| **ITIL** | IT Infrastructure Library | The service management framework |
| **ITSCM** | IT Service Continuity Management | The practice as a whole |
| **ITSCP** | IT Service Continuity Plan | A service-level plan under ITIL. Aligns to the ISCP structure without being one |
| **MM** | Maturity Model | As in the ITIL Maturity Model |
| **MTD** | Maximum Tolerable Downtime | How long a business process can be down before the consequences become unacceptable. A business number |
| **NIST** | National Institute of Standards and Technology |  |
| **NOC** | network operations center |  |
| **OEP** | Occupant Emergency Plan | Outside ISCP scope |
| **OLA** | operational level agreement |  |
| **OMB** | Office of Management and Budget |  |
| **OS** | operating system |  |
| **POA&M** | Plan of Action and Milestones | The tracked gap item opened when a requirement cannot be met |
| **PSF** | practice success factor | ITIL 4 term |
| **RPO** | Recovery Point Objective | How much committed work the business can afford to lose. The objective, not the outcome |
| **RTO** | Recovery Time Objective | How long until the system is technically available again |
| **SLA** | service level agreement |  |
| **SP** | Special Publication | As in NIST SP 800-34 |
| **SSP** | System Security Plan | The ISCP is Appendix G of one |
| **SVS** | Service Value System | ITIL 4 term |
| **UTC** | Coordinated Universal Time | The one clock every measurement in an IT skill is recorded against |
| **WRT** | Work Recovery Time | Technically available to actually usable: replaying interfaces, reconciling, finishing a close. Not a NIST term |

## Three pairs that get confused

**RPO against data loss.** The RPO is the objective, what the business will accept losing. Data
loss is the outcome, what a mechanism would actually cost on the day. They are compared, never
equated: a system with a five minute RPO that loses eight seconds met its objective, and one
with a zero RPO that loses eight seconds did not.

**RTO against MTD.** The RTO ends when the system is technically available. The MTD ends when
the business is running again. The gap between them is real work, and the RTO must be shorter
than the MTD because of it.

**ISCP against ITSCP.** An ISCP is a system-level artifact under NIST and FedRAMP. An ITSCP is a
service-level artifact under ITIL that may align to the ISCP structure without being one. A
DRP, BCP or COOP is none of the above.

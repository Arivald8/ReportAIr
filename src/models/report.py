from dataclasses import dataclass

@dataclass
class Report:
    reports_row_id: int = None
    report_id: int = None
    subject: str = None
    word_count: int = None
    student_id_ref: int = None
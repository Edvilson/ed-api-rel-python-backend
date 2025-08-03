from app.db import query_report
from app.models.report_model import ReportModel

def get_reports(data_inicial=None, data_final=None):
    columns, rows = query_report(data_inicial, data_final)
    reports = []
    idx_map = {col: idx for idx, col in enumerate(columns)}
    for row in rows:
        report = ReportModel(
            id=row[idx_map['ID']],
            nome=row[idx_map['NOME']],
            data_evento=row[idx_map['DATA_EVENTO']],
            valor=row[idx_map['VALOR']]
        )
        reports.append(report)
    return reports

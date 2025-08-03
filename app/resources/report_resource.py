from flask_restful import Resource, reqparse
from flasgger import swag_from
from app.services.report_service import get_reports
from app.schemas.report_schema import ReportSchema

class ReportResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data_inicial', type=str, required=False)
    parser.add_argument('data_final', type=str, required=False)

    @swag_from({
        'tags': ['Relatório'],
        'parameters': [
            {'name': 'data_inicial', 'in': 'query', 'type': 'string'},
            {'name': 'data_final', 'in': 'query', 'type': 'string'}
        ],
        'responses': {
            200: {
                'description': 'Lista de relatórios',
                'schema': ReportSchema(many=True)
            }
        }
    })
    def get(self):
        args = self.parser.parse_args()
        reports = get_reports(args['data_inicial'], args['data_final'])
        schema = ReportSchema(many=True)
        return schema.dump(reports), 200

from marshmallow import Schema, fields

SUCCESS = "000"
FAILURE = "001"
UNAUTHORIZED = "002"
NOT_FOUND = "003"

class ApiResponse:
    def __init__(self, response_code, message, data, page=1, pagination_limit=10):
       self.response_code = response_code
       self.message = message
       data_is_list = isinstance(data, list)
       self.length = len(data) if data_is_list else (1 if data else 0)
       self.page = page
       self.data = list(data[(page -1)*pagination_limit:page*pagination_limit]) if data_is_list else data


class ApiResponseSchema(Schema):
    response_code = fields.Str()
    message = fields.Str()
    data = fields.Raw()
    page = fields.Int()
    length = fields.Int()


api_response_schema = ApiResponseSchema()

def handleResponse(message, data, response_code, http_status_code):
     return api_response_schema.dump(
        ApiResponse(
            response_code,
            message,
            data
        )
    ), http_status_code
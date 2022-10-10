from validator.validationexception import ValidationException

class Validator:
    @staticmethod
    def validate_user_input(row, column):
        errors = []
        row_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        column_list = [1, 2, 3, 4, 5, 6, 7, 8]
        if row not in row_list:
            errors.append("invalid row!")
        if column not in column_list:
            errors.append("invalid column!")
        if len(errors) > 0:
            raise ValidationException(errors)

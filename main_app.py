from flask import Flask, request
from flask_restful import Resource, Api
import json
from PyPDF2 import  PdfWriter, PdfReader
from sys import platform

app = Flask(__name__)
api = Api(app)

class PDFroter(Resource):
    def post(self):
        """Roate nth page only"""
        try:
            req_data = json.loads(request.data.decode('utf-8'))

            file_path = req_data['file_path']
            rot_angle = req_data['rot_ang']
            page_num = req_data['page_num']

            # rotate angle check
            if rot_angle not in [90, 180, 270]:
                return ({'Error':'Rotation angle should be 90, 180 or 270'}, 400)
            reader = PdfReader(file_path, 'rb')
            writer = PdfWriter()
            total_pages = len(reader.pages)

            # page inbound check
            if page_num > total_pages:
                return ({'Error':'Page number is greater or smaller than total pages'}, 400)

            for page in range(total_pages):
                writer.add_page(reader.pages[page])
                if page_num-1 == page:
                    writer.pages[page].rotate(rot_angle)

            if platform == "linux" or platform == "darwin":
                # linux
                file_name = "".join(file_path.split("/")[-1].split(".")[0])
                roated_file_path = "/".join(file_path.split("/")[:-1])
                roated_file_name = '{}_rotated.pdf'.format(file_name)
                rot_full_path = "{}/{}".format(roated_file_path, roated_file_name)

            elif platform == "windows":
                # windows
                file_name = "".join(file_path.split("\\")[-1].split(".")[0])
                roated_file_path = "\\".join(file_path.split("\\")[:-1])
                roated_file_name = '{}_rotated.pdf'.format(file_path)
                rot_full_path = "{}\\{}".format(roated_file_path, roated_file_name)
            
            print(roated_file_name)
            with open(rot_full_path, 'wb') as f:
                writer.write(f)
            ret_data = {
                'Success':'File rotated successfully',
                'Rotated_File_path':rot_full_path
            }
            return (ret_data, 200)
        except Exception as e:
            return ({"Error":str(e)}, 400)
    
    def get(self):
        """Roate upto nth page"""
        print('test')
        req_data = request.args
        print(req_data)
        for i in req_data:
            if i not in ['file_path', 'rot_ang', 'page_num']:
                return ({'Error':'Invalid key, use keys:- file_path, rot_ang, page_num'}, 400)
            
        file_path = req_data['file_path']
        rot_angle = int(req_data['rot_ang'])
        page_num = int(req_data['page_num'])
        print(file_path, rot_angle, page_num)

        # rotate angle check
        if rot_angle not in [90, 180, 270]:
            return ({'Error':'Rotation angle should be 90, 180 or 270'}, 400)
        print('debug 2')

        try:
            reader = PdfReader(file_path, 'rb')
            writer = PdfWriter()
            total_pages = len(reader.pages)

            # page inbound check
            if page_num > total_pages:
                return ({'Error':'Page number is greater or smaller than total pages'}, 400)

            for page in range(total_pages):
                writer.add_page(reader.pages[page])
                if page < page_num:
                    writer.pages[page].rotate(rot_angle)

            if platform == "linux" or platform == "darwin":
                # linux
                file_name = "".join(file_path.split("/")[-1].split(".")[0])
                roated_file_path = "/".join(file_path.split("/")[:-1])
                roated_file_name = '{}_rotated.pdf'.format(file_name)
                rot_full_path = "{}/{}.pdf".format(roated_file_path, roated_file_name)

            elif platform == "windows":
                # windows
                file_name = "".join(file_path.split("\\")[-1].split(".")[0])
                roated_file_path = "\\".join(file_path.split("\\")[:-1])
                roated_file_name = '{}_rotated.pdf'.format(file_path)
                rot_full_path = "{}\\{}.pdf".format(roated_file_path, roated_file_name)
            
            print(roated_file_name)
            with open(rot_full_path, 'wb') as f:
                writer.write(f)
            ret_data = {
                'Success':'File rotated successfully',
                'Rotated_File_path':rot_full_path
            }
            return (ret_data, 200)
        except Exception as e:
            return ({"Error":str(e)}, 400)

        

api.add_resource(PDFroter, '/pdf/')
if __name__ == '__main__':
    app.run(debug=True)
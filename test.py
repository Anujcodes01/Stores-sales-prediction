# # testing  logging

# from flask import Flask
# from src.logger import logging

# app = Flask(__name__)

# @app.route('/', methods = ['GET', 'POST'])
# def index():
#     logging.info("We are testing our logging file")

#     return "Welcome to my new project "

# if __name__ == "__main__":
#     app.run(debug = True) # 5000


# # testng exceptions

# from flask import Flask
# from src.logger import logging
# from src.exception import CustomException
# import os, sys

# app = Flask(__name__)

# @app.route('/', methods = ['GET', 'POST'])
# def index():
    
#     try:
#         raise Exception('testing exception file')#error
#     except Exception as e:
#         ML = CustomException(e,sys)
        
#         logging.info(ML.error_message)
        
#         logging.info('we are testing our logging file ')
        
#         return "welcome to the application "
    
# if __name__=="__main__":
#     app.run(debug=True)## default port 5000
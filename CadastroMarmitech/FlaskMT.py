 app = Flask(__name__, static_url_path='')
  
  UPLOAD_FOLDER = 'static/uploads/'
 ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
 app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
 
 def allowed_file(filename):
     return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
     
 @app.route('/uploads/<filename>')
  def uploaded_file(filename):
      return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
      
 -                               
 +                             
  @app.route('/', methods=['POST','GET'])
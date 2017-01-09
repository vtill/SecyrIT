from bottle import route, run, static_file
import mimetypes,os

folder_root  = os.getcwd()
folder_files = '%s/files' % folder_root


def index_html():
    filename = 'index.html'
    mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    return static_file(filename, root=folder_root, mimetype=mt)

def send_image(filename):
    mt = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    return static_file(filename, root=folder_files, mimetype=mt)
      
def get_status():
    fname = '%s/statusfile' % os.getcwd()
    return  '{"status": "%s"}' % str(os.path.exists(fname)) 

def hello():
    return "Hello World!"

def index():
    return "index Hello World!"


#@route('/')
#@route('/files/<filename:re:.*\.*>')
#@route('/status')
#route('/',callback=blubb)
#route('/','GET',index)

route('/','GET',index_html)
route('/a','GET',index)
route('/files/<filename:re:.*\.*>','GET',send_image)
route('/status','GET',get_status)


run(host='10.254.239.1', port=8080, debug=True)

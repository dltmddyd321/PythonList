from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

# CoAP에서 자원은 무엇인가?
# 자원은 등록 / 수정 / 조회 / 삭제 가능한 대상 = IoT 자원

# 클래스 자원을 등록
class HelloWorldResource(Resource):
    def __init__(self, name="hello-world", coap_server=None):
        super(HelloWorldResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Getting!"

    def render_GET(self, request):
        self.payload = "Hello!"
        return self

class PingResource(Resource):
    def __init__(self, name="ping", coap_server=None):
        super(PingResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)

    def render_GET(self, request):
        self.payload = "Pong!"
        return self    

# 서버
class CoAPServer(CoAP):
    def __init__(self,host,port) :
        CoAP.__init__(self,(host,port))
        # 자원 추가
        self.add_resource('hello-world/', HelloWorldResource())
        self.add_resource('ping/', PingResource())
    
if __name__ == '__main__' :
    server = CoAPServer("0.0.0.0", 5671)
    try:
        print("서버 작동")
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("실행 중...")



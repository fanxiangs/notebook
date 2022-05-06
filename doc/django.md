<extoc></extoc>

## 请求生命周期

1. 用户输入网址，浏览器发起请求
2. WSGI（服务器网关接口）创建socket服务端，接受请求
3. 中间件处理请求
4. url路由，根据当前请求的url找到相应的视图函数
5. 进入view，进行业务逻辑处理，如果有数据的交互通过orm，model
6. 再次通过中间件处理相应数据
7. WSGI返回响应
8. 浏览器渲染

## django中间件的5个方法
1. process_request : 请求进来时,权限认证
2. process_view : 路由匹配之后,能够得到视图函数
3. process_exception : 异常时执行
4. process_template_responseprocess : 模板渲染时执行
5. process_response : 请求有响应时执行

## django 内置的缓存机制？
全站缓存、视图缓存、模版缓存

## django rest framework框架中都有那些组件？
1. 序列化组件:serializers  对queryset序列化以及对请求数据格式校验
2. 路由组件routers 进行路由分发
3. 视图组件ModelViewSet  帮助开发者提供了一些类，并在类中提供了多个方法
4. 认证组件 写一个类并注册到认证类(authentication_classes)，在类的的authticate方法中编写认证逻
5. 权限组件 写一个类并注册到权限类(permission_classes)，在类的的has_permission方法中编写认证逻辑。
6. 频率限制 写一个类并注册到频率类(throttle_classes)，在类的的allow_request/wait 方法中编写认证逻辑
7. 解析器  选择对数据解析的类，在解析器类中注册(parser_classes)
8. 渲染器 定义数据如何渲染到到页面上,在渲染器类中注册(renderer_classes)
9. 分页  对获取到的数据进行分页处理, pagination_class
10. 版本  版本控制用来在不同的客户端使用不同的行为 
在url中设置version参数，用户请求时候传入参数。在request.version中获取版本，根据版本不同 做不同处理
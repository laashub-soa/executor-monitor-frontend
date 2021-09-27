def init(app):
    from rest import ping
    from rest import service_frontend

    # ################### 注册路由
    app.register_blueprint(ping.app)
    app.register_blueprint(service_frontend.app)

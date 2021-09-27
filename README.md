# executor-monitor-frontend
executor-monitor-frontend





```
--------------------------------------------------------------------------------------------------- 前端请求
抓取策略:
	总是记录住用户在系统做的最近几个动作作为事件, 固定长度的队列, 事件的架构思路为 目标+动作+数据, 其中动作默认为click
	每10s汇聚发送一次, 并裁剪请求数据包大小, 每30s持久化一下
	超过1s钟的性能才作为慢性能

请求参数中的log、time、status可以为数组类型, 表示合并请求

请求参数: 
	replicaset			服务名称(英文简称)
	code_version		代码版本(数字以及字母)
	store_id			公司id
	user_id				用户id, 可以空传
	auth_token			登录token, 可以空传
	event				最近的事件, 例如: [{"t":"xxx", "d":"xxx"}]

	log					当为异常日志时的日志内容, 例如: ["xxx"]
	time				当为异常性能时的性能耗费时间(单位毫秒), 例如: [1500, 1600]
	metric				指标状态, 例如[{cpu: 80%, memory: 80%， network: 80%}]
--------------------------------------------------------------------------------------------------- 后端服务
# web页面专用
/service_frontend_error_log_web
/service_frontend_slow_trace_web
# app专用
/service_frontend_slow_trace_app
/service_frontend_slow_trace_app

服务端地址?
service_frontend_monitor.dev.local.wangjiahuan.com
service_frontend_monitor.stage.local.wangjiahuan.com
service_frontend_monitor.wangjiahuan.com
--------------------------------------------------------------------------------------------------- 后端存储
--------------------------------- 前端错误日志
"job": service_frontend_log_error
"environment": ""
"replicaset": ""
"code_version": ""
"device": ""
"timestamp": ""
"value": {
	"store_id"
	"user_id"
	"event"
	"log"
}
--------------------------------- 前端慢性能
"job": service_frontend_trace_slow
"environment": ""
"replicaset": ""
"code_version": ""
"device": ""
"timestamp": ""
"value": {
	"store_id"
	"user_id"
	"event"
	"time"
}
--------------------------------- 前端差状态
"job": service_frontend_metric_bad
"environment": ""
"replicaset": ""
"code_version": ""
"device": ""
"timestamp": ""
"value": {
	"store_id"
	"user_id"
	"event"
	"metric"
}





```


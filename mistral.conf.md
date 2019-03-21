[DEFAULT]
transport_url = rabbit://openstack:Welcome123@controller:5672/
[cors]
[database]
connection = mysql+pymysql://mistral:Welcome123@controller:3306/mistral
[keystone_authtoken]
www_authenticate_uri = http://controller:5000/v3
auth_uri = http://controller:5000/v3
identity_uri = http://controller:5000
auth_version = v3
admin_user = mistral
admin_password = Welcome123
admin_tenant_name = service
[matchmaker_redis]
[oslo_messaging_amqp]
[oslo_messaging_kafka]
[oslo_messaging_notifications]
[oslo_messaging_rabbit]
[oslo_messaging_zmq]
[oslo_policy]
policy_file = /etc/mistral/policy.json
[ssl]

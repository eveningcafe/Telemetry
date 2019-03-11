Ceilometer là một dịch vụ thu thập dữ liệu, sử dụng để thu thập, chuẩn hóa, vận chuyển dữ liệu trên các OpenStack core components. 

Dữ liệu lấy về nhằm mục đích customer billing, resource tracking, and alarming với các OpenStack core components. 

Các function:
- Polls metering data related to OpenStack services.
- Collects event and metering data by monitoring notifications sent from services.
- Publishes collected data to various targets including data stores and message queues.

Các thành phần:
- Compute agent (ceilometer-agent-compute): chạy trên các compute node , lấy các resource utilization statistics, "This is actually the polling agent ceilometer-polling running with parameter --polling-namespace compute"

- Central agent (ceilometer-agent-central): chạy trên central management server, để polling resource khác instances or compute nodes."This is actually the polling agent ceilometer-polling running with parameter --polling-namespace central."

- Notification agent (ceilometer-agent-notification): chạy trên central management server, lấy thông tin từ messages từ the message queue cho các event and metering data. Sau đó bắn về 1 service khác, mà mặc định trong mô hình chuẩn là gnocchi

Ceilometer thiết kế có thể published to various endpoints for storage and analysis.

Giới thiệu:
 Ceilometer project  khởi đầu năm  2012 với mục tiêu: cung cấp khả năng thu thập bất kỳ thông tin cần từ các OpenStack projects. 
  Thiết kế: " rating engines could use this single source to transform events into billable items which we label as “metering”.".
 Sau đó: "become a standard way to meter, regardless of the purpose of the collection".
 
 3 bước: 
    Metering <-- ultimate goal
    
    Rating
    
    Billing
(các khái niệm ở https://docs.openstack.org/ceilometer/latest/glossary.html#term-rating)

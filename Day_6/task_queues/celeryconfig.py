broker_url = 'amqp://guest@localhost//'
imports = ('simple_tasks',)
#result_backend = 'db+sqlite:///results.db'
result_backend = 'redis://localhost/0'
#task_annotations = {'tasks.add': {'rate_limit': '10/s'}}
#task_compression = "bzip2"
task_publish_retry = True
task_publish_retry_policy = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.8,
}
task_track_started = True
task_soft_time_limit = 20
task_time_limit = 25
task_acks_late = True
task_reject_on_worker_lost = True

# 若只想发出警告，指出情况偏离了正轨，可使用模块warnings中的函数warn
# 警告类似于异常，但通常只打印一条错误消息
from warnings import warn
from warnings import filterwarnings

warn("I've got a bad feeling about this.")

# filterwarnings可抑制发出的警告，并指定要采取的措施，如“error”或“ignore”
filterwarnings('ignore')
warn("anyone out there?")

filterwarnings('error')
warn("something is very wrong.")
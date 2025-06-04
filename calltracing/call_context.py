import inspect
from typing import Optional

class CallContext:
    @staticmethod
    def get_caller(skip_frames: int = 0) -> Optional[str]:
        try:
            frame = inspect.currentframe()
            for _ in range(skip_frames + 1):
                if frame is None:
                    return '<module>'
                frame = frame.f_back

            if frame is None:
                return '<module>'

            caller_name = frame.f_code.co_name

            if 'self' in frame.f_locals:
                self_obj = frame.f_locals['self']
                return f'{self_obj.__class__.__name__}.{caller_name}'
            
            if 'cls' in frame.f_locals:
                cls_obj = frame.f_locals['cls']
                return f'{cls_obj.__name__}.{caller_name}'
            
            if '.' in frame.f_code.co_qualname:
                class_name = frame.f_code.co_qualname.split('.')[0]
                return f'{class_name}.{caller_name}'
            
            return caller_name if caller_name != '<module>' else '<module>'

        finally:
            del frame
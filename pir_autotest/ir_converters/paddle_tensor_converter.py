import pir_autotest.ir.ir_type as ir_type
import pir_autotest.ir.ir_tensor as ir_tensor
import pir_autotest.ir_converters.paddle_type_converter as paddle_type_converter

def ConvertToPaddleTensor(tensor):
  return ir_tensor.Tensor(
    local_name_prefix=tensor.local_name_prefix,
    name=tensor.name,
    type=ir_type.DenseTensorType(
      tensor.shape,
      paddle_type_converter.ConvertTypeToString(tensor.dtype)
    )
  )
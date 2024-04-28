from dataclasses import dataclass
import pir_autotest.ir.ir_op as ir_op
from pir_autotest.ir_converters.paddle_tensor_converter import ConvertToPaddleTensor

@dataclass
class Op(ir_op.Op):

  def GetResult(self, i):
    return ConvertToPaddleTensor(ir_op.Op.GetResult(self, i))
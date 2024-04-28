from pir_autotest.traits.args_trait import ArgsTrait
from pir_autotest.traits.type_trait import TypeTrait
from pir_autotest.traits.attr_trait import AttrTrait
from pir_autotest.traits.op_trait import OpTrait
from pir_autotest.generators.fusion_op_unittest_generator import (
  FusionOpUnittestGenerator
)

class Program(ArgsTrait, OpTrait, TypeTrait, AttrTrait):

  def __init__(self):

    self.data_46 = self.Op("pd_op.data", 46, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), shape=self.a_intarray(1), name=self.a_str("arg_0"), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.data_47 = self.Op("pd_op.data", 47, input_types=[], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), shape=self.a_intarray(1), name=self.a_str("arg_1"), place=self.a_place("undefined", 0), dtype=self.a_dtype("bool")))

    self.exp_71 = self.Op("pd_op.exp", 71, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.subtract_72 = self.Op("pd_op.subtract", 72, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.scale_73 = self.Op("cinn_op.scale", 73, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(bias=self.a_f32("0"), stop_gradient=self.a_array(self.a_bool(True)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1")))

    self.scale_74 = self.Op("cinn_op.scale", 74, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(bias=self.a_f32("1"), stop_gradient=self.a_array(self.a_bool(True)), bias_after_scale=self.a_bool(True), scale=self.a_f32("1")))

    self.yield_76 = self.Op("cf.yield", 76, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict())

    self.fusion_75 = self.Op("cinn_op.fusion", 75, input_types=[], output_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_bool())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.reduce_sum_77 = self.Op("cinn_op.reduce_sum", 77, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([], self.t_f32())], attrs=dict(keep_dim=self.a_bool(False), stop_gradient=self.a_array(self.a_bool(True)), dim=self.a_array()))

    self.full_78 = self.Op("pd_op.full", 78, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("0"), shape=self.a_intarray(1), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.broadcast_79 = self.Op("cinn_op.broadcast", 79, input_types=[self.t_dtensor([], self.t_f32())], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), out_shape=self.a_array(self.a_i64(1)), broadcast_axes=self.a_array()))

    self.greater_than_80 = self.Op("pd_op.greater_than", 80, input_types=[self.t_dtensor([1], self.t_f32()), self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.full_81 = self.Op("pd_op.full", 81, input_types=[], output_types=[self.t_dtensor([1], self.t_f32())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True)), value=self.a_f32("1"), shape=self.a_intarray(1), place=self.a_place("undefined", 0), dtype=self.a_dtype("float32")))

    self.cast_82 = self.Op("pd_op.cast", 82, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(dtype=self.a_dtype("bool"), stop_gradient=self.a_array(self.a_bool(True))))

    self.less_than_83 = self.Op("pd_op.less_than", 83, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.logical_and_84 = self.Op("pd_op.logical_and", 84, input_types=[self.t_dtensor([1], self.t_bool()), self.t_dtensor([1], self.t_bool())], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(stop_gradient=self.a_array(self.a_bool(True))))

    self.yield_86 = self.Op("cf.yield", 86, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict())

    self.fusion_85 = self.Op("cinn_op.fusion", 85, input_types=[], output_types=[self.t_dtensor([1], self.t_bool())], attrs=dict(group_info=self.a_group_info()), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    self.shadow_output_62 = self.Op("builtin.shadow_output", 62, input_types=[self.t_dtensor([1], self.t_f32())], output_types=[], attrs=dict(output_name=self.a_str("output_0")))

    self.shadow_output_63 = self.Op("builtin.shadow_output", 63, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict(output_name=self.a_str("output_1")))

    self.shadow_output_64 = self.Op("builtin.shadow_output", 64, input_types=[self.t_dtensor([1], self.t_bool())], output_types=[], attrs=dict(output_name=self.a_str("output_2")))

    self.module_44 = self.Op("builtin.module", 44, input_types=[], output_types=[], attrs=dict(program=self.a_pointer("0x47043780")), block_positional_arg_names=[[[]]], block_keyword_arg_names=[[{}]])

    

  def fusion_75_block00(self, call, data_460, data_470):

    def ret_lambda():

      exp_710, = call(self.exp_71, data_460)

      subtract_720, = call(self.subtract_72, exp_710, data_460)

      scale_730, = call(self.scale_73, data_470)

      scale_740, = call(self.scale_74, scale_730)

      return call(self.yield_76, subtract_720, scale_740)

    return ret_lambda

    

  def fusion_85_block00(self, call, fusion_750, fusion_751):

    def ret_lambda():

      reduce_sum_770, = call(self.reduce_sum_77, fusion_750)

      full_780, = call(self.full_78)

      broadcast_790, = call(self.broadcast_79, reduce_sum_770)

      greater_than_800, = call(self.greater_than_80, broadcast_790, full_780)

      full_810, = call(self.full_81)

      cast_820, = call(self.cast_82, full_810)

      less_than_830, = call(self.less_than_83, fusion_751, cast_820)

      logical_and_840, = call(self.logical_and_84, greater_than_800, less_than_830)

      return call(self.yield_86, logical_and_840)

    return ret_lambda

    

  def module_44_block00(self, call):

    def ret_lambda():

      data_460, = call(self.data_46)

      data_470, = call(self.data_47)

      fusion_750, fusion_751, = call(self.fusion_75, blocks=[[(self.fusion_75_block00, data_460, data_470)]])

      fusion_850, = call(self.fusion_85, blocks=[[(self.fusion_85_block00, fusion_750, fusion_751)]])

      call(self.shadow_output_62, fusion_750)

      call(self.shadow_output_63, fusion_751)

      call(self.shadow_output_64, fusion_850)

    return ret_lambda

    

  def __call__(self, call, *args, **kwargs):

    self.SetArgs(args)

    self.SetKeywordArgs(kwargs)

    return call(self.module_44, blocks=[[(self.module_44_block00,)]])


if __name__ == "__main__":
  ir_program = Program()
  generator = FusionOpUnittestGenerator()
  op_name2unittest = generator.Generate(ir_program)
  for name, unittest in op_name2unittest.items():
    print("#", "="*80)
    print("#", name)
    print("#", "-"*80)
    print(unittest)
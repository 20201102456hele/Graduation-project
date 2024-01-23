<template>
  <Layer :layer="layer" @confirm="submit">
    <el-form :model="ruleForm" :rules="rules" ref="form" label-width="120px" style="margin-right:30px;">
      <el-form-item label="用户：" prop="username">
        <el-input v-model="ruleForm.username" placeholder="请输入用户"></el-input>
      </el-form-item>
      <el-form-item label="密码：" prop="password">
        <el-input v-model="ruleForm.password"  placeholder="请输入密码"></el-input>
      </el-form-item>


    </el-form>
  </Layer>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'
import Layer from '@/components/layer/index.vue'
import { add, update } from '@/api/system/user'
export default defineComponent({
  components: {
    Layer
  },
  props: {
    layer: {
      type: Object,
      default: () => {
        return {
          show: false,
          title: '',
          showButton: true
        }
      }
    }
  },
  setup(props, ctx) {
    let ruleForm = reactive({
      username: '',
      password: '',

    })
    const rules = {
      username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
      password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
    }

    return {
      ruleForm,
      rules
    }
  },
  methods: {
    submit() {
      this.$refs['form'].validate((valid: boolean) => {
        if (valid) {
          let params = this.ruleForm
          if (this.layer.row) {
            this.updateForm(params)
          } else {
            this.addForm(params)
          }
        } else {
          return false;
        }
      });
    },
    // 新增提交事件
    addForm(params: object) {
      add(params)
      .then(res => {
        this.$message({
          type: 'success',
          message: '新增成功'
        })
        this.layer.show = false
        this.$emit('getTableData', true)
      })
    },
    // 编辑提交事件
    updateForm(params: object) {
      update(params)
      .then(res => {
        this.$message({
          type: 'success',
          message: '编辑成功'
        })
        this.$emit('getTableData', false)
      })
    }
  }
})
</script>

<style lang="scss" scoped>

</style>

<template>
  <Layer :layer="layer" @confirm="submit" ref="layerDom">
    <el-form :model="form" :rules="rules" ref="ruleForm" label-width="120px" style="margin-right:30px;">
      <el-form-item label="软件名称：" prop="name">
        <el-input v-model="form.name" placeholder="请输入名称"></el-input>
      </el-form-item>
      <el-form-item label="评论：" prop="comment">
        <el-input v-model="form.comment"  placeholder="请输入评论信息"  @blur="analysis(form.comment)"></el-input>
      </el-form-item>

      <el-form-item label="评论类型：" prop="commentType">
        <el-input v-model="form.commentType"  placeholder="等待模型生成评论结果" disabled></el-input>
      </el-form-item>

    </el-form>
  </Layer>
</template>

<script lang="ts">
import type { LayerType } from '@/components/layer/index.vue'
import type { Ref } from 'vue'
import type { ElFormItemContext } from 'element-plus/lib/el-form/src/token'
import { defineComponent, ref } from 'vue'
import {analysisCommentApi, addCommentApi} from '@/api/table'
import { selectData, radioData } from './enum'
import Layer from '@/components/layer/index.vue'
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
    const ruleForm: Ref<ElFormItemContext|null> = ref(null)
    const layerDom: Ref<LayerType|null> = ref(null)
    let form = ref({
      name: '',
      comment: '',
      commentType: '',
    })
    const rules = {
      name: [{ required: true, message: '请输入软件名称', trigger: 'blur' }],
      comment: [{ required: true, message: '请输入评论', trigger: 'blur' }],
      commentType: [{ required: true, message: '等待模型生成评论类型', trigger: 'blur' }],
    }
    init()
    function init() { // 用于判断新增还是编辑功能
      if (props.layer.row) {
        form.value = JSON.parse(JSON.stringify(props.layer.row)) // 数量量少的直接使用这个转
      } else {

      }
    }
    return {
      form,
      rules,
      layerDom,
      ruleForm,
      selectData,
      radioData
    }
  },

  methods: {

    analysis(comment: string){
      analysisCommentApi({comment: comment}).then(res=>{
        console.log(res.data)
        this.form.commentType = res.data
      })

    },

    submit() {
      if (this.ruleForm) {
        this.ruleForm.validate((valid) => {
          if (valid) {
            let params = this.form
            if (this.layer.row) {
              // this.updateForm(params)
            } else {
              this.addForm(params)
            }
          } else {
            return false;
          }
        });
      }
    },
    // 新增提交事件
    addForm(params: object) {
      addCommentApi(params)
      .then(res => {
        this.$message({
          type: 'success',
          message: '新增成功'
        })
        this.$emit('getTableData', true)
        this.layerDom && this.layerDom.close()
      })
    },
    // 编辑提交事件
    // updateForm(params: object) {
    //   update(params)
    //   .then(res => {
    //     this.$message({
    //       type: 'success',
    //       message: '编辑成功'
    //     })
    //     this.$emit('getTableData', false)
    //     this.layerDom && this.layerDom.close()
    //   })
    // }
  }
})
</script>

<style lang="scss" scoped>

</style>

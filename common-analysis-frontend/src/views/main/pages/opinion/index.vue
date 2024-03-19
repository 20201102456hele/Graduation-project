<template>
  <div class="layout-container">
    <div class="layout-container-form flex space-between">
      <div class="layout-container-form-handle">
        <el-button type="primary" :icon="Plus" @click="handleAdd" v-if="store.state.user.info === 'he'">新增</el-button>

      </div>
      <div class="layout-container-form-search">
        <el-input v-model="query.name" placeholder="请输入关键字查询" @change="getTableData(true)"></el-input>
        <el-button type="primary" :icon="Search" class="search-btn" @click="getTableData(true)">搜索</el-button>
      </div>
    </div>
    <div class="layout-container-table">
      <Table
        ref="table"

        v-loading="loading"
        :showIndex="true"
        :showSelection="true"
        :data="tableData"
        @getTableData="getTableData"
        @selection-change="handleSelectionChange"
      >
        <el-table-column prop="software" label="软件名称" align="center" />
        <el-table-column prop="info" label="评论" align="center" />
<!--        <el-table-column prop="user" label="用户" align="center" />-->

      </Table>
      <Layer :layer="layer" @getTableData="getTableData" v-if="layer.show" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref, reactive } from 'vue'
import Table from '@/components/table/index.vue'
import {getOpinionApi} from '@/api/table'
import Layer from './layer.vue'
import { ElMessage } from 'element-plus'
import type { LayerInterface } from '@/components/layer/index.vue'
import { Plus, Search, Delete } from '@element-plus/icons'
import {useStore} from "vuex";


const store = useStore()
// 存储搜索用的数据
const query = reactive({
  name: ''
})
// 弹窗控制器
const layer: LayerInterface = reactive({
  show: false,
  title: '新增',
  showButton: true
})

const loading = ref(true)
const tableData = ref([])
const chooseData = ref([])
const handleSelectionChange = (val: []) => {
  chooseData.value = val
}
// 获取表格数据
// params <init> Boolean ，默认为false，用于判断是否需要初始化分页
const getTableData = (init: boolean) => {
  loading.value = true

  getOpinionApi(query.name)
  .then(res => {

    tableData.value = res.data
  })
  .catch(error => {
    tableData.value = []

  })
  .finally(() => {
    loading.value = false
  })
}

// 新增弹窗功能
const handleAdd = () => {
  layer.title = '新增反馈意见'
  layer.show = true
  delete layer.row
}
// // 编辑弹窗功能
// const handleEdit = (row: object) => {
//   layer.title = '编辑数据'
//   layer.row = row
//   layer.show = true
// }
getTableData(true)

</script>

<style lang="scss" scoped>

</style>

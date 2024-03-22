<template>
  <div class="layout-container">
    <div class="layout-container-form flex space-between">
      <div class="layout-container-form-handle">
        <el-button type="primary" :icon="Plus" @click="handleAdd"  v-if="store.state.user.info === 'he'">新增</el-button>
<!--        <el-popconfirm :title="$t('message.common.delTip')" @confirm="handleDel(chooseData)">-->
<!--          <template #reference>-->
<!--            <el-button type="danger" :icon="Delete" :disabled="chooseData.length === 0">{{ $t('message.common.delBat') }}</el-button>-->
<!--          </template>-->
<!--        </el-popconfirm>-->
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
        <el-table-column prop="name" label="软件名称" align="center" />
        <el-table-column prop="info" label="评论" align="center" />
        <el-table-column prop="comment_type" label="评论类型" align="center" />

<!--        <el-table-column prop="radioName" label="单选框" align="center" />-->
<!--        <el-table-column :label="$t('message.common.handle')" align="center" fixed="right" width="200">-->
<!--          <template #default="scope">-->
<!--            <el-button @click="handleEdit(scope.row)">{{ $t('message.common.update') }}</el-button>-->
<!--            <el-popconfirm :title="$t('message.common.delTip')" @confirm="handleDel([scope.row])">-->
<!--              <template #reference>-->
<!--                <el-button type="danger">{{ $t('message.common.del') }}</el-button>-->
<!--              </template>-->
<!--            </el-popconfirm>-->
<!--          </template>-->
<!--        </el-table-column>-->
      </Table>
      <Layer :layer="layer" @getTableData="getTableData" v-if="layer.show" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineComponent, ref, reactive } from 'vue'
import Table from '@/components/table/index.vue'
import {getCommentApi} from '@/api/table'
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

  getCommentApi(query.name)
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
  layer.title = '新增评论'
  layer.show = true
  delete layer.row
}
// 编辑弹窗功能
const handleEdit = (row: object) => {
  layer.title = '编辑数据'
  layer.row = row
  layer.show = true
}
getTableData(true)

</script>

<style lang="scss" scoped>

</style>

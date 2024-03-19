<template>

  <div class="layout-container">

    <el-form :model="ruleForm"  label-width="100px" class="demo-ruleForm" style="margin-top: 20px">
      <el-form-item label="用户名">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm()">查询</el-button>
      </el-form-item>
    </el-form>

    <div class="category" id="main"  style="height: 800px;width: 100%;margin-top: 20px">
    </div>
    <div class="category2" id="main2"  style="height: 800px;width: 100%;margin-top: 20px">

    </div>

  </div>

</template>

<script lang="ts" setup>
import { onMounted, reactive, ref} from 'vue'
import {getCommentAnalysisApi} from '@/api/table'
import * as echarts from 'echarts';

const ruleForm = reactive({
  name: "支付宝"
})

const submitForm = () =>{
  getData(ruleForm.name)
}

const state = reactive({
  dataX: [],
  dataY: []
})

onMounted(()=>{
  getData(ruleForm.name)

})

const getData = (name: string) => {
  getCommentAnalysisApi(name)
      .then(res => {
        state.dataX = res.data.godDataX
        state.dataY = res.data.godDataY

        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom);
        var option;
        option = {
          title: {
            text: '好评关键词',
            left: 'center'
          },
          xAxis: {
            type: 'category',
            data: state.dataX
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: state.dataY,
              type: 'line'
            }
          ]
        };
        option && myChart.setOption(option);

        var chartDom = document.getElementById('main2');
        var myChart = echarts.init(chartDom);
        var option;
        option = {
          title: {
            text: '差评关键词',
            left: 'center'
          },
          xAxis: {
            type: 'category',
            data: res.data.badDataX
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              data: res.data.badDataY,
              type: 'line'
            }
          ]
        };
        option && myChart.setOption(option);


      })
}


</script>

<style lang="scss" scoped>

</style>

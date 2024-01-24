import type { Route } from '../index.type'
import Layout from '@/layout/index.vue'
import { createNameComponent } from '../createNode'
const route: Route[] = [
  {
    path: '/tools',
    component: Layout,
    redirect: '/tools/timestamp',
    meta: { title: '常用工具', icon: 'sfont system-component' },
    alwayShow: true,
    children: [
      {
        path: 'timestamp',
        component: createNameComponent(() => import('@/views/main/tools/timestamp/index.vue')),
        meta: { title: '时间戳转换' }
      },
      {
        path: 'dateCompute',
        component: createNameComponent(() => import('@/views/main/tools/dateCompute/index.vue')),
        meta: { title: '日期差计算' }
      },
      {
        path: 'codeTransform',
        component: createNameComponent(() => import('@/views/main/tools/codeTransform/index.vue')),
        meta: { title: 'unicode互转' }
      },
      {
        path: 'jsonAnalysis',
        component: createNameComponent(() => import('@/views/main/tools/jsonAnalysis/index.vue')),
        meta: { title: 'json解析' },
      },
      {
        path: 'jsonPath',
        component: createNameComponent(() => import('@/views/main/tools/jsonPath/index.vue')),
        meta: { title: 'jsonpath在线测试' },
      },
      {
        path: 'textDiff',
        component: createNameComponent(() => import('@/views/main/tools/textDiff/index.vue')),
        meta: { title: '文本diff' },
      },
      {
        path: 're',
        component: createNameComponent(() => import('@/views/main/tools/reTest/index.vue')),
        meta: { title: '正则表达式在线测试' },
      },
      {
        path: 'orCode',
        component: createNameComponent(() => import('@/views/main/tools/orCode/index.vue')),
        meta: { title: '二维码生成' },
      },
      {
        path: 'md5',
        component: createNameComponent(() => import('@/views/main/tools/md5/index.vue')),
        meta: { title: 'md5加解密' },
      },
      {
        path: 'http',
        component: createNameComponent(() => import('@/views/main/tools/http/index.vue')),
        meta: { title: 'http接口' },
      }

    ]
  }
]

export default route

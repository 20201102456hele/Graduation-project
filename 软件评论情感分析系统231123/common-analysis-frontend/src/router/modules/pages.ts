import type { Route } from '../index.type'
import Layout from '@/layout/index.vue'
import { createNameComponent } from '../createNode'
const route: Route[] = [
  {
    path: '/pages',
    component: Layout,
    redirect: '/pages/comment',
    meta: { title: '数据相关', icon: 'sfont system-page' },
    alwayShow: true,
    children: [
      {
        path: 'comment',
        component: createNameComponent(() => import('@/views/main/pages/comment/index.vue')),
        meta: { title: '评论数据', cache: false, roles: ['admin', 'editor'] }
      },

      {
        path: 'zhu',
        component: createNameComponent(() => import('@/views/main/pages/zhu/index.vue')),
        meta: { title: '柱状图' }
      },

      {
        path: 'ciyun',
        component: createNameComponent(() => import('@/views/main/pages/ciyun/index.vue')),
        meta: { title: '词云图' }
      },

      {
        path: 'dataAnalysis',
        component: createNameComponent(() => import('@/views/main/pages/dataAnalysis/index.vue')),
        meta: { title: '数据分析' }
      },

      {
        path: 'opinion',
        component: createNameComponent(() => import('@/views/main/pages/opinion/index.vue')),
        meta: { title: '反馈意见' }
      }

    ]

  }

]

export default route

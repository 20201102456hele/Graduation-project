import type { Route } from '../index.type'
import Layout from '@/layout/index.vue'
import { createNameComponent } from '../createNode'
const route: Route[] = [

  {
    path: '/collect',
    component: Layout,
    redirect: '/collect',
    meta: { title: '', icon: 'sfont system-page' },
    children: [
      {
        path: 'collect',
        component: createNameComponent(() => import('@/views/main/dashboard/collect/index.vue')),
        meta: { title: '收藏', icon: 'sfont system-page', hideClose: true }
      }
    ]
  }
]

export default route

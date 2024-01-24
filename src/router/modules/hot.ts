import type { Route } from '../index.type'
import Layout from '@/layout/index.vue'
import { createNameComponent } from '../createNode'
const route: Route[] = [

  {
    path: '/hot',
    component: Layout,
    redirect: '/hot',
    meta: { title: '', icon: 'sfont system-component' },
    children: [
      {
        path: 'hot',
        component: createNameComponent(() => import('@/views/main/dashboard/hot/index.vue')),
        meta: { title: '热门', icon: 'sfont system-component', hideClose: true }
      }
    ]
  }
]

export default route

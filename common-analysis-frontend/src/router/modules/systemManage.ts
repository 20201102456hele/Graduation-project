import type { Route } from '../index.type'
import Layout from '@/layout/index.vue'
import { createNameComponent } from '../createNode'
const route: Route[] = [
  {
    path: '/systemManage',
    component: Layout,
    redirect: '/systemManage/menu',
    meta: { title: 'message.menu.systemManage.name', icon: 'sfont system-xitongzhuangtai' },
    alwayShow: true,
    children: [
      {
        path: 'user',
        component: createNameComponent(() => import('@/views/main/systemManage/users/index.vue')),
        meta: { title: '用户信息' }
      }
    ]
  }
]

export default route

import Vue from 'vue'
import Router from 'vue-router'
// import search from '@/components/Search'

const routerOptions = [{
  path: '/',
  component: 'Home'
},
{
  path: '/about',
  component: 'About'
},
{
  path: '*',
  component: 'NotFound'
},
{
  path: '/hello',
  component: 'Hello'
},
{
  path: '/user',
  component: 'User'
},
{
  path: '/search',
  name: 'search',
  component: 'Search'
},
{
  path: '/search01',
  name: 'search',
  component: 'search01'
},
{
  path: '/msp',
  name: 'msp',
  component: 'Msp'
}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})

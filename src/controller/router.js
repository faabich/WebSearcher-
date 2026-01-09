import { createRouter, createWebHistory } from 'vue-router'

import SearchHistory from 'src/components/SearchHistory.vue'


const routes = [
    {
        path: '/',
        name: 'Home Page',
        component: SearchHistory
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
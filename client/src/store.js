import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('chef_token') || '',
        user: {},
        recipies: [],
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token) {
            state.status = 'success'
            state.token = token
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        SET_RECIPIES(state, recipies) {
            state.recipies = recipies;
        }
    },
    actions: {
        login({commit}, data) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url: 'http://127.0.0.1:5000/auth/login', data: data, method: 'POST'})
                .then(response => {
                    const chef_token = response.data.Data.chef_token
                    localStorage.setItem('chef_token', chef_token)
                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + chef_token
                    commit('auth_success', chef_token)
                    resolve(response)
                })
                .catch(error => {
                    commit('auth_error')
                    localStorage.removeItem('chef_token')
                    reject(error)
                })
            })
        },
        register({commit}, data) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                axios({url: 'http://127.0.0.1:5000/auth/register', data: data, method: 'POST'})
                .then(response => {
                    // const chef_token = response.data.Data.chef_token
                    // localStorage.setItem('chef_token', chef_token)
                    // axios.defaults.headers.common['Authorization'] = 'Bearer ' + chef_token
                    commit('auth_success', '')
                    resolve(response)
                })
                .catch(error => {
                    commit('auth_error')
                    localStorage.removeItem('chef_token')
                    reject(error)
                })
            })
        },
        logout({commit}) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('chef_token')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
        fetchRecipies({commit}) {
            return new Promise((resolve, reject) => {
                axios({url: 'http://127.0.0.1:5000/recipe/', method: 'GET'})
                .then(response => {
                    commit('SET_RECIPIES', response.data['Data'])
                    resolve(response)
                })
            })
        },
        createRecipe({commit}, data) {
            return new Promise((resolve, reject) => {
                console.log(data)
                axios({url: 'http://127.0.0.1:5000/recipe/', data: data, method: 'POST'})
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
            })
        },
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status
    }
})
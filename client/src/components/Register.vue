<template>
    <div>
        <UserForm :actionButtonTitle="'Register'" @action-button-clicked="register"></UserForm>    
    </div>    
</template>
<script>
import UserForm from './UserForm.vue'
export default {
    name: 'Register',
    components: {
        UserForm
    },
    methods: {
        register(data) {
            this.$store.dispatch('register', data)
            .then(response => {
                console.log(response.data)
                this.$router.push({name: 'Home'})
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>
<style scoped>

</style>

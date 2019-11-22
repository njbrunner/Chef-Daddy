<template>
    <div>
        <UserForm :actionButtonTitle="'Login'" @action-button-clicked="login"></UserForm>
    </div>
</template>
<script>
import UserForm from './UserForm.vue'
export default {
    name: 'Login',
    components: {
        UserForm
    },
    data ()  {
        return {
        }
    },
    methods: {
        login(data) {
            this.$store.dispatch('login', data)
            .then(response => {
                console.log(response.data['Message']);
                this.$router.push({name: 'Home'});
            })
            .catch(error => {
                console.log(error);
            })
        }
    }
}
</script>
<style scoped>

</style>

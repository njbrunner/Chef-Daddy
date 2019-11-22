<template>
    <div class="page">
        <div class="row">
            <div class="col-md-3">
                <router-link to="/recipe/new" class="btn btn-outline-success">Create New Recipe</router-link>
            </div>
            <div class="col-md-9">
                <recipe-list-item v-for="recipe in recipies" :recipe="recipe" :key="recipe._id"></recipe-list-item>
            </div>    
        </div>  
    </div>    
</template>
<script>
import CreateRecipeForm from './CreateRecipeForm.vue'
import RecipeListItem from './RecipeListItem.vue'
import axios from 'axios'
export default {
    name: 'Home',
    components: {
        CreateRecipeForm,
        RecipeListItem
    },
    data() {
        return {
            recipies: []
        }
    },
    created() {
        this.$store.dispatch('fetchRecipies')
        .then(response => {
            this.recipies = response.data['Data'];
        })
        .catch(error => {
            console.log(error.response.data)
        })
    }
}
</script>
<style scoped>
.page {
    margin-top: 60px;
}
</style>

<template>
    <div class="container">
        <h4><b>New Recipe</b></h4>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Name" v-model="name">
            <br>
            <textarea class="form-control" placeholder="Description" v-model=summary></textarea>
        </div>
        <div class="ingredient-form">
            <h5><b>Ingredients</b></h5>
            <IngredientForm @addIngredient="addIngredient"></IngredientForm>
        </div>
        <table class="table" v-if="ingredients.length > 0">
            <thead>
                <th scope='column'>Name</th>
                <th scope='column'>Quantity</th>
                <th scope='column'>Measurement</th>
                <th></th>
            </thead>
            <tbody>
                <Ingredient v-for="(ingredient, index) in ingredients" :key=index :ingredient="ingredient" @remove=removeIngredient(index)></Ingredient>
            </tbody>
        </table>
        <button class="btn btn-outline-primary float-right" v-if="recipeValid" @click="submitRecipe">Save</button>
    </div>
</template>
<script>
import IngredientForm from './IngredientForm.vue'
import Ingredient from './Ingredient.vue'
export default {
    name: 'CreateRecipeForm',
    components: {
        IngredientForm,
        Ingredient
    },
    data() {
        return {
            'name': null,
            'summary': null,
            'ingredients': [],
        }
    },
    methods: {
        addIngredient(ingredientData) {
            this.ingredients.push(ingredientData)
        },
        removeIngredient(index) {
            console.log('test')
            this.ingredients.splice(index, 1);
        },
        submitRecipe() {
            var data = {
                name: this.name,
                summary: this.summary,
                ingredients: this.ingredients
            }
            this.$store.dispatch('createRecipe', data)
            .then(response => {
                console.log(response)
                this.$router.push({name: 'Home'})
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
    computed: {
        recipeValid() {
            return (this.ingredients.length > 0)
        }
    }
}
</script>
<style scoped>
table {
    margin-top: 32px;
    margin-bottom: 32px;
}

.ingredient-form {
    margin-top: 32px;
}
</style>

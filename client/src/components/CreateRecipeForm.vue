<template>
    <div class="container">
        <h4><b>New Recipe</b></h4>
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Name" v-model="name">
            <br>
            <input type="file" accept="image/*" class="image-upload" @change="uploadImage($event)">
            <textarea class="form-control" placeholder="Description" v-model=description></textarea>
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
            'description': null,
            'ingredients': [],
        }
    },
    methods: {
        addIngredient(ingredientData) {
            this.ingredients.push(ingredientData)
        },
        removeIngredient(index) {
            this.ingredients.splice(index, 1);
        },
        submitRecipe() {
            var data = {
                name: this.name,
                description: this.description,
                ingredients: this.ingredients
            }
            this.$store.dispatch('createRecipe', data)
            .then(response => {
                this.$toasted.show(response.data['Message'], {type: 'success'})
                this.$router.push({name: 'Home'})
            })
            .catch(error => {
                console.log(error.response.data['Message'])
                this.$toasted.show(error.response.data['Message'], {type: 'error'})
            })
        },
        uploadImage(event) {
            console.log("Image upload");
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

.image-upload {
    background: transparent;
}
</style>

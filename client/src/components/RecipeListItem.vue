<template>
    <div class="row">
        <div class="col-md-6">
            {{recipe.name}}
        </div>
        <div class="col-md-6">
            {{recipe.ingredients.length}}
        </div>    
    </div>
</template>
<script>
export default {
    name: 'RecipeListItem',
    props: {
        recipe: Object
    },
    data() {
        return {
        }
    },
}
</script>
<style scoped>
</style>

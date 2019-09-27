<template>
    <tr>
        <th scope="row">{{ ingredient.name }}</th>
        <td>{{ ingredient.quantity }}</td>
        <td>{{ ingredient.measurement }}</td>
        <td><button class="btn btn-outline-danger" @click="remove"><i class="far fa-trash-alt"></i></button></td>
    </tr>
</template>
<script>
export default {
    name: 'Ingredient',
    props: {
        ingredient: Object
    },
    methods: {
        remove() {
            this.$emit('remove');
        }
    }
}
</script>
<style scoped>

</style>
<template>
  <div id="app">
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm @create-todo="createTodo"/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [  ]
    }
  },
  methods: {
    createTodo (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo)
    },
    deleteTodo (todo) {
      // 1. 인덱스 배열을 찾기
      const index = this.todos.indexOf(todo)
      
      // 2. 인덱스 삭제하고 다시 배열 만들기
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style>


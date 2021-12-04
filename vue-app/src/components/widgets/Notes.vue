<template>
  <v-card
    class="mx-auto"
    height="500"
    style="overflow: auto"

    elevation="24"
    :shaped="true"
    :rounded="true"
  >
    <v-card-title>{{$t('Ultimas Mudanças')}}</v-card-title>
    <v-card-text>
      <v-list three-line>
        <template v-for="(item, index) in items">
          <v-divider
            v-if="item.divider"
            :key="index"
            :inset="item.inset"
          ></v-divider>

          <v-list-item
            v-else
            :key="index"
          >
            <v-list-item-avatar>
              <v-icon>{{item.icon}}</v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card-text>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      items: [
        {
          icon: 'mdi-store-plus',
          title: 'Saída de estoque',
          subtitle: 'Estoque de sadasdsa aumentou',
        },
        { divider: true, inset: true },
        {
          icon: 'mdi-cash-plus',
          title: 'Recebimento de pagamento',
          subtitle: 'fulano da silva te pagou',
        },
        { divider: true, inset: true },
        {
          icon: 'mdi-store-plus',
          title: 'Saída de estoque',
          subtitle: 'Estoque de sadasdsa aumentou',
        },
        { divider: true, inset: true },
        {
          icon: 'mdi-cash-plus',
          title: 'Recebimento de pagamento',
          subtitle: 'fulano da silva te pagou',
        },
        {
          icon: 'mdi-store-plus',
          title: 'Saída de estoque',
          subtitle: 'Estoque de sadasdsa aumentou',
        },
        { divider: true, inset: true },
        {
          icon: 'mdi-cash-plus',
          title: 'Recebimento de pagamento',
          subtitle: 'fulano da silva te pagou',
        },
      ],
    }),
  }
</script>

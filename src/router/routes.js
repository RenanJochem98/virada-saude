const routes = [
  {
    path: "/",
    component: () => import("layouts/IndexLayout.vue"),
    children: [{ path: "", component: () => import("pages/Index.vue") }],
  },
  {
    path: "/Questionario",
    component: () => import("layouts/DefaultLayout.vue"),
    children: [{ path: "", name: "Questionario", component: () => import("pages/Questionario.vue") }],
  },
  {
    path: "/Home",
    component: () => import("layouts/HomeLayout.vue"),
    children: [{ path: "", name: "Home", component: () => import("pages/Home.vue") }],
  },
  {
    path: "/ProximoTreino",
    component: () => import("layouts/HomeLayout.vue"),
    children: [{ path: "", name: "ProximoTreino", component: () => import("pages/ProximoTreino.vue") }],
  },
  {
    path: "/Treino",
    component: () => import("layouts/HomeLayout.vue"),
    children: [{ path: "", name: "Treino", component: () => import("pages/Treino.vue") }],
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;

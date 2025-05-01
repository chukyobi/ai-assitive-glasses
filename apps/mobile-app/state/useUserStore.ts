import { create } from 'zustand';

type UserStore = {
  name: string;
  setName: (name: string) => void;
};

export const useUserStore = create<UserStore>((set) => ({
  name: 'Guest',
  setName: (name) => set({ name }),
}));

import { View, ScrollView } from 'react-native';
import Header from '@/components/Header';
import NotificationCard from '@/components/NotificationCard';
import { useEffect, useState } from 'react';
import { fetchNotifications } from '@/services/notificationService';

export default function NotificationsScreen() {
  const [notifications, setNotifications] = useState<any[]>([]);

  useEffect(() => {
    fetchNotifications().then(setNotifications);
  }, []);

  return (
    <ScrollView style={{ padding: 16 }}>
      <Header title="Notifications" />
      {notifications.map((note, index) => (
        <NotificationCard key={index} title={note.title} message={note.message} />
      ))}
    </ScrollView>
  );
}

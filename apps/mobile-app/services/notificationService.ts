const DUMMY_NOTIFICATIONS = [
    { title: 'Update Available', message: 'A new firmware update is ready to install.' },
    { title: 'Battery Low', message: 'Please recharge your assistive glasses.' },
  ];
  
  export const fetchNotifications = async () => {
    // Simulated delay
    await new Promise((res) => setTimeout(res, 500));
    return DUMMY_NOTIFICATIONS;
  };
  
  export const sendNotification = async (title: string, message: string) => {
    console.log('Sending:', { title, message });
    return { success: true };
  };
  
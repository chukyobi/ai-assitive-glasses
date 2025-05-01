// app/services/firmwareService.ts
import apiClient from './apiClient';

export async function getLatestFirmwareVersion() {
  const res = await apiClient.get('/firmware/latest');
  return res.data;
}

export async function triggerFirmwareUpdate(deviceId: string) {
  const res = await apiClient.post(`/firmware/update`, { deviceId });
  return res.data;
}

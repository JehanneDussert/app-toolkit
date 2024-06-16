import { useState, useCallback } from 'react';

export const useFetch = (url: string) => {
	const [data, setData] = useState<any>(null);
	const [error, setError] = useState<any>(null);
	const [loadingData, setLoadingData] = useState<boolean>(false);

	const fetchData = useCallback(
		async (query: string, num_results: number = 10) => {
			setLoadingData(true);

			try {
				const response = await fetch(
					`${url}?query=${query}&num_results=${num_results}`
				);

				if (!response.ok) {
					throw new Error(
						`Fetch failed with status: ${response.status}`
					);
				}

				const data = await response.json();

				setData(data);
			} catch (error) {
				setError(error);
			} finally {
				setLoadingData(false);
			}
		},
		[url]
	);

	return { data, error, loadingData, fetchData };
};

import { useState } from 'react';
import { useFetch } from '../utils/hooks';
import { Cards } from '../components/Cards';
import { Searchbar } from '../components/Searchbar';
import Pagination from '@mui/material/Pagination';

export const Home = () => {
	const [query, setQuery] = useState<string>('');
	const [isSubmitted, setIsSubmitted] = useState<boolean>(false);
	const [currentPage, setCurrentPage] = useState<number>(1);
	const itemsPerPage = 5;
	const { error, loadingData, fetchData } = useFetch('/');
	const data = ["test 1", "test 2", "test 3", "test 4", "test 5", "test 6", "test 7"];

	const handlePageChange = (event: React.ChangeEvent<unknown>, page: number) => {
		setCurrentPage(page);
	};

	if (loadingData)
		return (
			<div className="flex justify-center items-center w-full">
				Chargement de la page...
			</div>
		);
	if (error) return <div>Erreur : {error.message}</div>;

	const offset = (currentPage - 1) * itemsPerPage;
	const currentPageItems = data.slice(offset, offset + itemsPerPage);

	return (
		<div className="w-full flex items-center flex-col">
			<div className="w-11/12 mb-8">
				<Searchbar
					query={query}
					setIsSubmitted={setIsSubmitted}
					handleChange={(e: React.ChangeEvent<HTMLInputElement>) => 
						setQuery(e.target.value)
					}
				/>
				{/* <ParamsMenu /> */}
				<Cards currentPageItems={currentPageItems} />
				<Pagination 
					count={Math.ceil(data.length / itemsPerPage)}
					page={currentPage}
					onChange={handlePageChange}
					variant="outlined"
				/>
			</div>
		</div>
	);
};

